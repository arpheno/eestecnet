/**
 * Created by swozn on 9/18/2015.
 */
describe('the page', function () {
    beforeEach(function () {
        browser.get('http://172.17.42.1:8000/', 15000);
    });
    it('should login a user', function () {
        element(by.css('[aria-label="Login"]')).click();
        expect(element(by.css('md-dialog')).isDisplayed()).toBeTruthy();
        var username = element(by.model('login.email'));
        var password = element(by.model('login.password'));
        username.sendKeys('admin@eestec.net');
        password.sendKeys('1234');
        element(by.id('loginbutton')).click();
        element(by.css('[aria-label="Manage your Account"]')).click();
        expect(element(by.css('md-menu')).isDisplayed()).toBeTruthy();
    });
});
