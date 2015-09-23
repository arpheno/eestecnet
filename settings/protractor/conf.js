/**
 * Created by swozn on 9/18/2015.
 */
exports.config = {
    seleniumAddress: 'http://localhost:4444/wd/hub',
    specs: ['../../**/spec.js'],
    capabilities: {
        browserName: 'chrome',
        idleTimeout: 30,
        baseUrl: 'http://172.17.42.1:8000/'
    },
    params: {
        admin: {
            user: 'admin@eestec.net',
            password: '1234'
        }
    }
};

