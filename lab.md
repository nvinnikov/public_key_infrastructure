Шаг 1: Создание корневого сертификата:
Первым шагом мы создаем корневой сертификат, который будет использоваться для подписи самоподписанных сертификатов. Мы можем использовать команду OpenSSL для создания корневого сертификата:

```
openssl req -x509 -new -key private.key -out root.crt
```

openssl: это имя самой команды, которая вызывает утилиту OpenSSL.
req: Этот аргумент указывает на использование подкоманды "req", которая отвечает за запросы на сертификаты.
-x509: Этот аргумент указывает на создание самозаверяющего сертификата (self-signed certificate) вместо запроса на сертификат (certificate request).
-new: Этот аргумент указывает на создание нового сертификата или запроса на сертификат. В данном случае, он означает создание нового самозаверяющего сертификата.
-key private.key: Этот аргумент указывает на использование файла private.key в качестве закрытого ключа (private key) для создания сертификата. Здесь предполагается, что файл private.key содержит закрытый ключ, необходимый для создания сертификата.
-out root.crt: Этот аргумент указывает на сохранение созданного сертификата в файл с именем root.crt. Здесь root.crt - это имя файла, в который будет сохранен самозаверяющий сертификат.

Таким образом, команда openssl req -x509 -new -key private.key -out root.crt создает самозаверяющий сертификат, используя закрытый ключ из файла private.key и сохраняет его в файл root.crt.
```
➜  ossl openssl req -x509 -new -key private.key -out root.crt
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []:RU
State or Province Name (full name) []:Moscow
Locality Name (eg, city) []:Moscow
Organization Name (eg, company) []:HSE
Organizational Unit Name (eg, section) []:MIEM
Common Name (eg, fully qualified host name) []:localhost
Email Address []:nvinnikov@miem.hse.ru
➜  ossl cat root.crt 
-----BEGIN CERTIFICATE-----
MIIDijCCAnICCQDpvIM0rJW9GzANBgkqhkiG9w0BAQsFADCBhjELMAkGA1UEBhMC
UlUxDzANBgNVBAgMBk1vc2NvdzEPMA0GA1UEBwwGTW9zY293MQwwCgYDVQQKDANI
U0UxDTALBgNVBAsMBE1JRU0xEjAQBgNVBAMMCWxvY2FsaG9zdDEkMCIGCSqGSIb3
DQEJARYVbnZpbm5pa292QG1pZW0uaHNlLnJ1MB4XDTIzMDYyMjE5MjY1OVoXDTIz
MDcyMjE5MjY1OVowgYYxCzAJBgNVBAYTAlJVMQ8wDQYDVQQIDAZNb3Njb3cxDzAN
BgNVBAcMBk1vc2NvdzEMMAoGA1UECgwDSFNFMQ0wCwYDVQQLDARNSUVNMRIwEAYD
VQQDDAlsb2NhbGhvc3QxJDAiBgkqhkiG9w0BCQEWFW52aW5uaWtvdkBtaWVtLmhz
ZS5ydTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANZlp+gvA1aaxScv
8VToQG4D0uSB2rY4zDCBJBEPnZmnpcimQnXJpgu0V/Y3KwTScUlc54r0jBA+YdVC
2lw/nVecUiGluuqHcP6z/VtAY9UOedeoyVYb5ns3+6MuYyk0M1L3OcoXOW0Kyz4y
SKbtF/bnxImhiEvvhkB0VNJ3e6gzcaCY7FgY8yfdV7EcEAjtc0CBv869E7dmZNW3
IYKTv7BXHoecaABnJ0wFztTj9q0pPjO1tR3DaEoKwT3mcj6owqeORaMiKLxsPckc
NQTub52VphBjF6BYCJlBwCr28gRoNOTjCNokBZl7m0og29rGDKnCsOSEsbpW5yMA
/QasCL0CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAdbI+/hFSxRzzraEgQceJ+Axs
wBtgvdJR8N4hfILkXdP2HCgEKrxoxwFkIDMqNvmbRkMamBh3W+nM1xz2Dkyxbqpg
M1CPu6OOU9NXMUkiOtbGtIbczdd2Eaw+TZD5ozXGzrTGiJWTsRL/FnG0NOPhQZC9
NUeJAiFC0clybv653dHRJJPm3PThtMRmoX8Amaz6UVJRPTt+U7dCQvpl6uSCP5pb
iLMVZGrK566Ke6SvgXRvGcJ/0WUGFWhJcsv8NfXYGqwLLRh5MJPzz9fad4W0fcRo
pT8WI2grW038V++J86vc+h2PXYut/GrBo1sxvfVMn6zVEP8CZ05j+dbOGr2mVQ==
-----END CERTIFICATE-----
```



При выполнении этой команды OpenSSL попросил ввести информацию о владельце корневого сертификата. Затем он создал файл `root.crt`, который будет содержать корневой сертификат.

Шаг 2: Подписание самоподписанного сертификата:
Затем мы подписываем самоподписанный сертификат с помощью корневого сертификата. Мы можем использовать команду OpenSSL для этого:
```
openssl x509 -req -in request.csr -CA root.crt -CAkey private.key -CAcreateserial -out certificate.crt
```
-req: Этот флаг указывает на то, что входной файл является запросом на сертификат (CSR).
-in request.csr: Этот аргумент задает входной файл request.csr, который содержит информацию о запросе на сертификат, отправленном к удостоверяющему центру (Certification Authority, CA).
-CA root.crt: Этот аргумент определяет файл корневого сертификата root.crt. Корневой сертификат представляет собой доверенный сертификат, используемый для проверки цепочки сертификации. Он является основой для создания сертификата, соответствующего запросу.
-CAkey private.key: Этот аргумент задает закрытый ключ private.key, который принадлежит удостоверяющему центру (CA) и используется для подписи сертификата.
-CAcreateserial: Этот флаг указывает на то, что серийный номер сертификата должен быть создан автоматически.
-out certificate.crt: Этот аргумент определяет выходной файл certificate.crt, в который будет сохранен созданный сертификат X.509.

Эта команда использует корневой сертификат и закрытый ключ для подписания самоподписанного сертификата, содержащегося в файле `request.csr`. Результат подписания сохраняется в файле `certificate.crt`.
```
➜  ossl 
openssl x509 -req -in request.csr -CA root.crt -CAkey private.key -CAcreateserial -out certificate.crt
Signature ok
subject=/C=RU/ST=Moscow/L=Moscow/O=MIEM/OU=HSE/CN=localhost/emailAddress=nvinnikov@miem.hse.ru
Getting CA Private Key
➜  ossl cat certificate.crt 
-----BEGIN CERTIFICATE-----
MIIDijCCAnICCQCtoxPMyyXycDANBgkqhkiG9w0BAQsFADCBhjELMAkGA1UEBhMC
UlUxDzANBgNVBAgMBk1vc2NvdzEPMA0GA1UEBwwGTW9zY293MQwwCgYDVQQKDANI
U0UxDTALBgNVBAsMBE1JRU0xEjAQBgNVBAMMCWxvY2FsaG9zdDEkMCIGCSqGSIb3
DQEJARYVbnZpbm5pa292QG1pZW0uaHNlLnJ1MB4XDTIzMDYyMjE5MjcyOFoXDTIz
MDcyMjE5MjcyOFowgYYxCzAJBgNVBAYTAlJVMQ8wDQYDVQQIDAZNb3Njb3cxDzAN
BgNVBAcMBk1vc2NvdzENMAsGA1UECgwETUlFTTEMMAoGA1UECwwDSFNFMRIwEAYD
VQQDDAlsb2NhbGhvc3QxJDAiBgkqhkiG9w0BCQEWFW52aW5uaWtvdkBtaWVtLmhz
ZS5ydTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANZlp+gvA1aaxScv
8VToQG4D0uSB2rY4zDCBJBEPnZmnpcimQnXJpgu0V/Y3KwTScUlc54r0jBA+YdVC
2lw/nVecUiGluuqHcP6z/VtAY9UOedeoyVYb5ns3+6MuYyk0M1L3OcoXOW0Kyz4y
SKbtF/bnxImhiEvvhkB0VNJ3e6gzcaCY7FgY8yfdV7EcEAjtc0CBv869E7dmZNW3
IYKTv7BXHoecaABnJ0wFztTj9q0pPjO1tR3DaEoKwT3mcj6owqeORaMiKLxsPckc
NQTub52VphBjF6BYCJlBwCr28gRoNOTjCNokBZl7m0og29rGDKnCsOSEsbpW5yMA
/QasCL0CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEALRivLhK8gLGaahSY7YiP4eak
7AxBexRE+fY7JPdShOwZXg9/NSQLS8FQb1CH9MxTISJorIJaNWMlEAyWBxjjIk1O
TpYYwqWkWdzC3BFnN0zXTU5MMU6++nHF5ziQQGsqH8LMMI2ExJio4IyOWsMGlFI4
7NRBq9iT54fmTrIwimSNG/+eN3r6oUJbJEZyEvl++pQlRpFMlmo/JKUY9M2/HxTj
33xEp5rklbJyGDX3C+Q9Kk4B/3SCuyPwfmxB2+B5Oqrpd57OH7m7Xg7377fsjEwb
HeS+8H+KgIjDP+t5NhqUkhp4loNzTlhNUWaL3nmgB46uBkMUTxg7vlXrcQxe4g==
-----END CERTIFICATE-----
```


Далее необходимо добавить сертификат в KeyChain (MacOS) и сделать его доверенным


В операционной системе Windows необходимо открыть "Управление компьютером" -> "Службы и приложения" -> "Сертификаты" -> "Доверенные корневые центры сертификации" и импортировать root.crt


