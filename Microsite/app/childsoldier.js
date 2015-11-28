angular.module('Eggly', [

])
    .controller('MainCtrl', function ($scope) {
        $scope.countries = [
            {"id": 0, "name": "Syria"},
            {"id": 1, "name": "Canada"},
            {"id": 2, "name": "USA"},
        ];

        $scope.reports = [
            {"id": 0, "title": "Report of Syria", "url": "http://angularjs.org", "country": "Syria" },
            {"id": 1, "title": "Report of Canada", "url": "http://angularjs.org", "country": "Canada" },
            {"id": 2, "title": "Report of USA", "url": "http://alistapart.com/", "country": "USA" },
        ];

        $scope.sections = [
          {"id": 0, "title": "Section of Syria report", "content": "this is only a test", "report": "Report of Syria" },
          {"id": 1, "title": "Section of Canada report", "content": "this is only a test", "report": "Report of Canada" },
          {"id": 2, "title": "Section of USA report", "content": "this is only a test", "report": "Report of USA" },
        ]

        $scope.isCreating = false;
        $scope.isEditing = false;
        $scope.currentCountry = null;

        function isCurrentCountry(country) {
            return $scope.currentCountry !== null && country.name === $scope.currentCountry.name;
        }

        function setCurrentCountry(country) {
            $scope.currentCountry = country;
            $scope.currentReport = null;
        }
      
        $scope.isCurrentCountry = isCurrentCountry;
        $scope.setCurrentCountry = setCurrentCountry;

      $scope.currentReport = null;
      function isCurrentReport(report) {
          return $scope.currentReport !== null && report.title === $scope.currentReport.title;
        }
  
        function setCurrentReport(report) {
          $scope.currentReport = report;
        }

        $scope.isCurrentReport = isCurrentReport;
        $scope.setCurrentReport = setCurrentReport;
    })
;