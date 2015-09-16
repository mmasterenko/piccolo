var app = angular.module('vapp', []);

app.controller('AssortController', function ($scope) {
    $scope.cookies = [
        [
            {
                img: '/media/images/middle/chertaldo.jpg',
                name: 'Чертальдо',
                pcs_weight: 2.5,
                weight_units: 'кг',
                pcs_per_box: 1.5,
                shelf_life: 45 + ' дней'
            },
            {
                img: '/media/images/middle/chertaldo.jpg',
                name: 'Чертальдо',
                pcs_weight: 2.5,
                weight_units: 'кг',
                pcs_per_box: 1.5,
                shelf_life: 45 + ' дней'
            },
            {
                img: '/media/images/middle/chertaldo.jpg',
                name: 'Чертальдо',
                pcs_weight: 2.5,
                weight_units: 'кг',
                pcs_per_box: 1.5,
                shelf_life: 45 + ' дней'
            }
        ]
    ]
});
