angular.module('reports', [
  'countries.reports.edit',
  'countries.reports.create',
  'childsoldier.models.countries',
  'childsoldier.models.reports'
])
  .config(function ($stateProvider) {
    $stateProvider
      .state('childsoldier.countries.reports', {
        url: 'countries/:country',
        views: {
          'reports@': {
            controller: 'reportsCtrl',
            templateUrl: 'app/countries/reports/reports.tmpl.html'
          }
        }
      })
    ;
  })
  .controller('reportsCtrl', function reportsCtrl($scope, $stateParams, reports, countries) {
    countries.setCurrentCountry();

    if ($stateParams.country) {
      countries.getCountryByName($stateParams.country).then(function (country) {
        countries.setCurrentCountry(country);
      })
    }

    reports.getreports()
      .then(function (result) {
        $scope.reports = result;
      });

    $scope.getCurrentCountry = countries.getCurrentCountry;
    $scope.getCurrentCountryName = countries.getCurrentCountryName;
    $scope.isSelectedReport = function (reportId) {
      return $stateParams.reportId == reportId;
    };

    $scope.deleteReport = reports.deleteReport;
  })
;

