angular.module('countries.reports.create', [
  'childsoldier.models.reports'
])
  .config(function ($stateProvider) {
    $stateProvider
      .state('childsoldier.countries.reports.create', {
        url: '/reports/create',
        views: {
          '@childsoldier.countries.reports': {
            templateUrl: 'app/countries/reports/create/create.report.tmpl.html',
            controller: 'CreateReportCtrl',
          }
        }
      })
    ;
  })

  .controller('CreateReportCtrl', function ($scope, $stateParams, reports, $state) {
    $scope.isCreating = false;

    function toggleCreating() {
      $scope.isCreating = !$scope.isCreating;
    }

    function returnToreports() {
      $state.go('childsoldier.countries.reports', {
        country: $stateParams.country
      })
    }

    function cancelCreating() {
      $scope.isCreating = false;
      returnToreports();
    }

    function createReport() {
      reports.createReport($scope.newReport);
      returnToreports();
    }

    function resetForm() {
      $scope.newReport = {
        title: '',
        url: '',
        country: $stateParams.country
      };
    }

    $scope.toggleCreating = toggleCreating;
    $scope.cancelCreating = cancelCreating;
    $scope.createReport = createReport;

    resetForm();
    toggleCreating();
  })
;
