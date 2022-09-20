window.onload = function () {
    $('#github').click(function(){
        var githubname=prompt("请输入用户名");
        chrome.storage.sync.set({'githubname':githubname});
        chrome.storage.sync.set({'flag':1});
        var githuburl1="https://api.github.com/users/"+githubname;
        // var githuburl2="https://api.github.com/users/"+githubname+"/following";
        // var githuburl3="https://api.github.com/users/"+githubname+"/followers";
        // var githuburl4="https://api.github.com/users/"+githubname+"/repos";
        // var githuburl5="https://api.github.com/users/"+githubname+"/received_events";
        window.open(githuburl1)

     //   chrome.storage.sync.set({ 'githubname': githubname })
    })


    $('#jianshu').click(function(){
        var jianshu=prompt("请输入用户的主页链接");
        var jianshuname="";
        var j=0;
        for(var i=0;i<jianshu.length;i++)
        {
                jianshuname=jianshuname.concat(jianshu[i]);
                if(jianshu[i]=='/')
                {
                    jianshuname="";
                }
        }
        chrome.storage.sync.set({'jianshuname':jianshuname});
        console.log(jianshuname)
        var jianshuurl1="https://www.jianshu.com/asimov/users/slug/"+jianshuname;
        var jianshuurl2="https://www.jianshu.com/asimov/users/slug/"+jianshuname+"/public_notes";
        window.open(jianshuurl1);
    })


    $('#cnblog').click(function(){
        var cnblog=prompt("请输入用户的博客来链接");
        console.log(cnblog)
        var cnblogname="";
        var j="";

        for(var i=0;i<cnblog.length;i++)
        {
            cnblogname=cnblogname.concat(cnblog[i]);
                if(cnblog[i+1]=='/')
                {

                   j=cnblogname;
                 //   console.log(cnblogname)
                    cnblogname="";
                    i++;
                }
        }
        console.log(j);
        chrome.storage.sync.set({'cnblogname':j});
        var cnblogurl1="https://home.cnblogs.com/u/"+j+"/";
        window.open(cnblogurl1);
    })

    $('#oschina').click(function(){
        var oschina=prompt("请输入用户的博客链接");
        console.log(oschina)
        var oschinaname="";
        var j="";
        for(var i=0;i<oschina.length;i++)
        {
            oschinaname=oschinaname.concat(oschina[i]);
            j=oschinaname;
                if(oschina[i+1]=='/')
                {

                    oschinaname="";
                    i++;
                }
        }
        //j=oschinaname;
        console.log(j);
        chrome.storage.sync.set({'oschinaname':j});
        var oschinaurl1="https://my.oschina.net/u/"+j+"/";
        window.open(oschinaurl1);
    })


}