__author__ = 'chrix'

import httplib2
from apiclient.discovery import build
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials


#Aqui se pone que es un canario, se usa el track rollout y se le pone el porcentaje de usuario
#solo se permiten del 5% al 50% para mayor del 50% ya se usa el track de production
TRACK = 'rollout'
USER_FRACTION = 0.1
SERVICE_ACCOUNT_EMAIL = (
    'AQUI VA LA CUENTA DE SERVICIO, ESTA SE OBTIENE EN LA CONSOLA DE GOOGLE')

def main():
  # trae la llave
  f = file('AQUI VA EL NOMBRE DEL ARCHIVO DE LA LLAVE EN FORMATO .P12', 'rb')
  key = f.read()
  f.close()
  credentials = ServiceAccountCredentials.from_p12_keyfile(SERVICE_ACCOUNT_EMAIL,'key.p12',scope = 'https://www.googleapis.com/auth/androidpublisher')

  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('androidpublisher', 'v2', http=http)


#Se enlista el nombre del paquete y el nombre del archivo que seran el canario
  package_name = 'AQUI VA EL NOMBRE DEL PAQUETE'
  apk_file = 'AQUI VA EL NOMBRE DEL ARCHIVO APK'

  try:
    edit_request = service.edits().insert(body={}, packageName=package_name)
    result = edit_request.execute()
    edit_id = result['id']
    print edit_id

    apk_response = service.edits().apks().upload(
        editId=edit_id, packageName=package_name, media_body=apk_file).execute()

    print 'Version code %d has been uploaded' % apk_response['versionCode']

    track_response = service.edits().tracks().update(
        editId=edit_id,
        track=TRACK,
        packageName=package_name,
        body={u'track': TRACK,
              u'userFraction': USER_FRACTION,
              u'versionCodes': [apk_response['versionCode']]}).execute()

    print 'Track %s is set for version code(s) %s' % (
        track_response['track'], str(track_response['versionCodes']))

    #Hay que hacer commit para que los cambios los vean los usuarios, sino vale madres

    commit_request = service.edits().commit(
        editId=edit_id, packageName=package_name).execute()

    print 'Edit "%s" has been committed' % (commit_request['id'])

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main()