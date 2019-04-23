var http=require("http");
var fs=require("fs");
var url=require("url");


function getRandImg(imglist) {
	var ranx = parseInt(Math.floor(Math.random() * (imglist.length)));

	return imglist[ranx].filename;
}

function readFileList(path) {

	var filesList = [];

	var files = fs.readdirSync(path);
	files.forEach(function (itm, index) {
		var stat = fs.statSync(path + itm);
		if (stat.isDirectory()) {
			readFileList(path + itm + "/", filesList)
		} else {
    
			var obj = {};//定义一个对象存放文件的路径和名字
			obj.path = path;//路径
			obj.filename = itm//名字
			filesList.push(obj);
		}
    
	});

	return filesList;
}

//Init
var r18imglist = readFileList("./img/");

console.log('server running');
http.createServer(function(req,res){

	var url=req.url;
	if(url.substring(1,7)==='random'){
			

			if (url.substring(8,11) === 'r18') {
				var imgname = "./img/" + getRandImg(r18imglist);
				console.log(imgname);
				fs.readFile(imgname,function(err,data){
					res.writeHead(200);
					res.end(data);
				});
			}
			else if (url.substring(8,14) === 'allage') {
				var allageimglist = readFileList("./pixivImg/");
				var imgname = "./pixivImg/" + getRandImg(allageimglist);
				console.log(imgname);
				fs.readFile(imgname,function(err,data){
					res.writeHead(200);
					res.end(data);
				});
			}
			else {
				res.writeHead(404);
				res.end();
			}
	}
	else {
		res.writeHead(404);
		res.end();
	}
}).listen(8003);
