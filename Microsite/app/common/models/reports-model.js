angular.module('childsoldier.models.reports', [

])
  .service('reports', function reportsService($http, $q) {
    var URLS = {
        FETCH: 'data/reports.json'
      },
      reports,
      reportsModel = this;

    function extract(result) {
      return result.data;
    }

    function cachereports(result) {
      reports = extract(result);
      return reports;
    }

    reportsModel.getreports = function () {
      return (reports) ? $q.when(reports) : $http.get(URLS.FETCH).then(cachereports);
    };

    function findReport(reportId) {
      return _.find(reports, function (report) {
        return report.id === parseInt(reportId, 10);
      })
    }

    reportsModel.getReportById = function (reportId) {
      var deferred = $q.defer();
      if (reports) {
        deferred.resolve(findReport(reportId))
      } else {
        reportsModel.getreports().then(function () {
          deferred.resolve(findReport(reportId))
        })
      }
      return deferred.promise;
    };

    reportsModel.createReport = function (report) {
      report.id = reports.length;
      reports.push(report);
    };

    reportsModel.updateReport = function (report) {
      var index = _.findIndex(reports, function (b) {
        return b.id == report.id
      });
      reports[index] = report;
    };

    reportsModel.deleteReport = function (report) {
      _.remove(reports, function (b) {
        return b.id == report.id;
      });
    };

    reportsModel.getreportsForCountry = function (country) {
      _.filter(reports, function (b) {
        return b.country == country;
      });
    };
  })
;