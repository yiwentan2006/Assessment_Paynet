
    This readme accompanies the PKCS#12 keystore that was generated for you on the Mastercard Developers portal. It provides details about its purpose and how you can access the contents.

    Mastercard uses OAuth 1.0a with body hash extension for securing its APIs. This requires every request to be signed with a private key. The ownership of this key proves your identity during the authentication process. You can find more details about this mechanism in the support article at the following URL:
    https://developer.mastercard.com/support-article/what-authentication-requirements-are-there-to-use-the-raw-rest-protocol

  The keystore accompanied by this readme contains a public/private key pair. The public key was shared with Mastercard during the generation process and will be used to verify the OAuth signature provided on every API call. The OAuth signature must be created using the private key inside the P12 keystore. Details below outline the password and alias (friendly name) of the private key that you will need in order to access it in the keystore.

  Keystore details
  ----------------
  Filename: Test_B-sandbox
  Password: keystorepassword
  Private key alias (friendly name): keyalias

  List keystore contents
  ----------------------
  Java keytool:
  keytool -storetype PKCS12 -list -keystore Test_B-sandbox.p12 -storepass keystorepassword -v

  OpenSSL:
  openssl pkcs12 -info -in Test_B-sandbox.p12 -password pass:keystorepassword
  