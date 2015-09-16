var app = angular.module('vapp', []);

app.controller('AssortController', function ($scope, $http) {
    $scope.cookies = [];

    $scope.change_category = function (cat_id) {
        $('#assort-block ul li').removeClass('x-active');
        $('#assort-block ul li a#' + cat_id).parent().addClass('x-active');
        $http.get("/api/" + cat_id).success(function(response){
                $scope.cookies = response;
            });
    };

    var id = $('#assort-block ul li a').first().attr('id');
    $scope.change_category(id);

});
