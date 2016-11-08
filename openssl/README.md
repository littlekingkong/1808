# OpenSSL 

1、用 OpenSSL， Linux 上自带，常用命令如下：

	-- 生成 RSA 私钥（传统格式的）

	openssl genrsa -out rsa_private_key.pem 1024

	-- 将传统格式的私钥转换成 PKCS#8 格式的（JAVA需要使用的私钥需要经过PKCS#8编码，PHP程序不需要，可以直接略过）

	openssl pkcs8 -topk8 -inform PEM -in rsa_private_key.pem -outform PEM -nocrypt

	-- 生成 RSA 公钥

	openssl rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem


2、加/解密内容太大时，使用分段加/解密

	//公钥分段加密

	$encrypted = [];

	$dataArray = str_split($data, 117);

	foreach($dataArray as $subData){
		$subEncrypted = null;
		openssl_private_encrypt($subData, $subEncrypted, $pub_key);
		$encrypted[] = $subEncrypted;
	}

	$encrypted = implode('', $encrypted);



	//私钥分段解密

	$decrypted = [];

	$dataArray = str_split($data, 128);

	foreach($dataArray as $subData){
		$subDecrypted = null;
		openssl_private_decrypt($subData, $subDecrypted, $pri_key); //公钥加密的内容通过私钥解密出来
		$decrypted[] = $subDecrypted;
	}

	$decrypted = implode('', $decrypted);


参照文章：

http://www.linuxidc.com/Linux/2015-08/120985.htm

http://www.codesec.net/view/203353.html

http://blog.csdn.net/nodeathphoenix/article/details/51647278
