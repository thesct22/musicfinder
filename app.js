const express=require("express");
const https=require("https");
const bodyParser=require("body-parser");
const app=express();
app.use(express.static("assets"));
app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
    res.send("On home root");
});

app.get("/soundcloud/recent", function(req, res){
    res.send("On /soundcloud/recent");
});

app.get("/soundcloud/popular", function(req, res){
    res.send("On /soundcloud/popular");
});

app.get("/spotify/playlists/recent", function(req, res){
    res.send("On /spotify/playlists/recent");
});

app.get("/spotify/playlists/popular", function(req, res){
    res.send("on /spotify/playlists/popular");
});

app.get("/spotify/artist/recent", function(req, res){
    res.send("On /spotify/artist/recent");
});

app.get("/spotify/artist/popular", function(req, res){
    res.send("on /spotify/artist/popular");
});


app.listen(process.env.PORT || 3000, function(){
    console.log("Server running on port 3000");
});