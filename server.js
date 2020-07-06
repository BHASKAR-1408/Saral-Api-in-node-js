
const express = require('express');
const fs = require("fs");
const app = express();
app.use(express.json());


var total_data = JSON.parse(fs.readFileSync('completedata.json'));

var listOfcourses = total_data[0]["courses"];



// 1.first end point to get all the data

app.get('/saral.navgurukul.org',(req,res)=>{
    for(i of listOfcourses){
        delete i.data;
    }
    res.send(listOfcourses);
});

// 2.Getting the data from specific ID with query

app.get('/saral.navgurukul.org/course',(req,res)=>{
    var id = req.query.id;
    for(i of listOfcourses){
        if(id == i.id){
            res.send(i);
        }
    }
});

// 3. end point to get specific content with query

app.get('/saral.navgurukul.org/course',(req,res)=>{
    var id = req.query.id;
    var slug = req.query.slug;
    for(i of listOfcourses){
        if(id == i.id){
            for(slugcontent of i.data){
                if(slug == slugcontent.slug){
                    res.send(slugcontent.content);
                }
                else{
                    for(subslug of slugcontent.childExercises){
                        if(slug == subslug.slug){
                            res.send(subslug.content);
                        }
                    }
                }
            }
        }
    }
});

app.listen(3000,(req,res)=>{
    console.log('server is working!');
});

// https://expressjs.com/en/guide/routing.html









