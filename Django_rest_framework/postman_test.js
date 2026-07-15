// Postman Test for /api/music-weather/<city>/
pm.test("Response contains temperature and description", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('temperature');
    pm.expect(jsonData).to.have.property('description');
});
