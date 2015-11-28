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

        $scope.isCreating = false;
        $scope.isEditing = false;
        $scope.currentCountry = null;
        $scope.editedReport = null;

        function isCurrentCountry(country) {
            return $scope.currentCountry !== null && country.name === $scope.currentCountry.name;
        }

        function setCurrentCountry(country) {
            $scope.currentCountry = country;
        }

        $scope.isCurrentCountry = isCurrentCountry;
        $scope.setCurrentCountry = setCurrentCountry;

        function isSelectedReport(reportId) {
            return $scope.editedReport !== null && $scope.editedReport.id === reportId;
        }

        $scope.isSelectedReport = isSelectedReport;
    })
;