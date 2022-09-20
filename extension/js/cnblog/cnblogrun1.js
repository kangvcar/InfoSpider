window.onload = function () {
    // for(var i=0;i<10;i++)
    // {
    //      console.log(document.getElementsByTagName('a')[i].outerHTML)
    //     console.log(js = document.getElementsByTagName('a')[i].getAttribute('href'));
    // }
   var data= Array();
    for(var i=12;i<=14;i++)
    {
        console.log(document.getElementsByClassName('text_gray')[i-11].innerHTML)
        data.push(document.getElementsByClassName('text_gray')[i-11].innerHTML)
        var s=document.getElementsByTagName('li')[i].innerHTML;
        var st="";
        for(var j=0;j<s.length;j++)
        {
            st=st.concat(s[j]);
            if(s[j]=='>')
            st="";
        }
        console.log(st)
        data.push(st);
    }
    for(var i=6;i<=11;i++)
    {
        console.log(document.getElementsByTagName('span')[i].innerHTML)
        data.push(document.getElementsByTagName('span')[i].innerHTML)
    }

    data.push("关注数")
    data.push(document.getElementById('following_count').innerHTML)
    data.push("粉丝数")
    data.push(document.getElementById('follower_count').innerHTML)
    console.log("关注数")
    console.log(document.getElementById('following_count').innerHTML)
    console.log("粉丝数")
    console.log(document.getElementById('follower_count').innerHTML)

    //  var Divs = new Array();
    //  Divs= Array.from(document.getElementsByClassName("avatar_name"))
    //  console.log(Divs);
    // console.log(document.getElementsByClassName("avatar_name"));
    chrome.storage.sync.set({'user':data})
    chrome.storage.sync.get('cnblogname',function(budget){
        var cnblogurl2="https://www.cnblogs.com/"+budget.cnblogname+"/";
        window.open(cnblogurl2)
    })

}