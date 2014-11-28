import LoginAndGrapeNewThings

renrenspider=LoginAndGrapeNewThings.spider('929431626@qq.com','wang4502')
renrenspider.login()
renrenspider.feed(renrenspider.file)
renrenspider.show()