function Page(url, rebuild){
    // url: string - URL from which to fetch data;
    // rebuild: function - function which builds html from container;
    var self = this;
    self.container = []; // data fetched will be saved here
    self.lastModified = 0;
    self.newModified = 0;
    self.url = url;
    self.rebuild = rebuild;
    self.hardfetch = function(data, status, xhr){
        console.log(self.url +" is out of date, getting new Data.");
        self.lastModified = self.newModified;
        self.container = data;
        self.rebuild();
    }
    self.check = function(message, text, response){
        console.log("Checking "+self.url+" for new data.");
        var header = response.getResponseHeader("Last-Modified");
        self.newModified = new Date(Date.parse(header));
        if(self.newModified > self.lastModified){
            $.getJSON(url, self.hardfetch);
        }
    }
    self.fetch = function (){
        $.ajax({
            type: "HEAD",
            async: true,
            url: self.url,
            success: self.check,
        });
    }
}
function current(which){
    history.pushState({"which":which},which,"/"+which+"/");
    $(".contents").hide();
    $("#"+which).show();
}
