/**
 * Created by swozn on 9/18/2015.
 */
describe('general functionality', function () {
    beforeEach(function(){
        console.log("before get");
        browser.get('http://172.17.42.1:8000/');
        console.log("after get");
    });
    it('displays the sidenav when the menubutton is clicked', function () {

        element(by.id('sidenavbutton')).click();
        expect(element(by.css('md-sidenav')).isDisplayed()).toBeTruthy();
    });
});
