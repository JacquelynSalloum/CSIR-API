angular.module('countries', [
  'childsoldier.models.countries'
])
  .config(function ($stateProvider) {
    $stateProvider
      .state('childsoldier.countries', {
        url: '/',
        views: {
          'countries@': {
            controller: 'countriesCtrl',
            templateUrl: 'app/countries/countries.tmpl.html'
          },
          'reports@': {
            controller: 'reportsCtrl',
            templateUrl: 'app/countries/reports/reports.tmpl.html'
          }
        }
      });
  })

  .controller('countriesCtrl', function countriesCtrl($scope, countries) {
    $scope.getCurrentCountryName = countries.getCurrentCountryName;

    countries.getcountries()
      .then(function (result) {
        $scope.countries = result;
      });

    $scope.isCurrentCountry = function (country) {
      return country.name === $scope.getCurrentCountryName();
    }
  })
;