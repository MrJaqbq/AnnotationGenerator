#!/bin/bash
conan remote add yage https://api.bintray.com/conan/bentoudev/yage
conan user -p H3l+NCd900ZcmlUtnbZmlzk6BbqeLlcSF45nEazC8+D3pbtsI0I7iIjTDVLR7Km6/0y2VHR5mOQ/+2ch9PAGP5JH+YDEYpY0pp3NbUM94binOsChMkq0vw7LDtMiaC3A6+2iGfdET8X7TNLBRRh19Rw0udcfLODKRMJUhBh6hiKVEpSYAl8seQSfuLuSXJWhHjr+3mk2nZkmAlBN4dJU919xy5196LlXH7VnEKjtUPf3a+5aDRVMw/wSrXG9vzD6Oqc6PzaOVEp4JmMfeDjqQn/lzH3Kf1GGAn+gP5kA7gkk8DdjBUpVJ0PQGSn1X7w2R+eYtVX93hd3LOYKrWYjnjMGPT/yi9xQEA/lQilsFj8PJThOgcoX+zDvF/DlgorI4Mh5IsBWovf/JFQGphTFQIBBSZcSg7OKILAJiJhm8XOZuZYpTUM1Msp31Z2oeqDtAchxT8HSEtbugBk5cCtxq4Eua9NFDJfLWgf4Wi0k0qfpTVAms29lr2g8PcCDExWTu89tWnLZVnO8Krsuw8MwLxgBnnZjOSsj4Zrq8XgoWFy7qOFFlNTwQLwxrq7yfZqPWKZJ2Hm3a4aGj4GxLgkPhpHK7Js2gfNFcSLK+68kreoWQqxFxTBFUqV7P96nc6AuDoPzVP4n8o7l53ap2/1s3hhZ7TJve3OmgCSEce4PgTg= -r yage bentoudev
conan upload Agnes/0.1@bentoudev/yage --all -r=yage