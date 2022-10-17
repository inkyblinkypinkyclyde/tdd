const assert = require('assert');
const Template = require('../template.js');

describe('template', function () {

    let template

    beforeEach(function () {
        template = new Template();
    });

    it('should return a string', function () {
        const string = template.templateFunction('string');
        assert.equal('string', string);
    })
}
)