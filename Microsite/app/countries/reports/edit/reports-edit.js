angular.module('countries.reports.edit', [
  'childsoldier.models.reports'
])
  .config(function ($stateProvider) {
    $stateProvider
      .state('childsoldier.countries.reports.edit', {
        url: '/reports/:reportId/edit',
        views: {
          '@childsoldier.countries.reports': {
            templateUrl: 'app/countries/reports/edit/edit.report.tmpl.html',
            controller: 'EditReportCtrl'
          }
        }
      })
    ;
  })

  .controller('EditReportCtrl', function ($scope, reports, $stateParams, $state) {
    $scope.isEditing = false;

    function returnToreports() {
      $state.go('childsoldier.countries.reports', {
        country: $stateParams.country
      })
    }

    reports.getReportById($stateParams.reportId).then(function (report) {
      if (report) {
        $scope.isEditing = true;
        $scope.report = report;
        $scope.editedReport = angular.copy($scope.report);
      } else {
        returnToreports();
      }
    });

    function toggleEditing() {
      $scope.isEditing = !$scope.isEditing;
    }

    function updateReport() {
      $scope.report = angular.copy($scope.editedReport);
      reports.updateReport($scope.editedReport);
      returnToreports();
    }

    function cancelEditing() {
      $scope.isEditing = false;
      returnToreports();
    }

    $scope.toggleEditing = toggleEditing;
    $scope.cancelEditing = cancelEditing;
    $scope.updateReport = updateReport;
  })

;
