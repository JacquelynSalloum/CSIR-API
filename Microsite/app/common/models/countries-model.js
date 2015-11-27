angular.module('childsoldier.models.countries', [

])
  .service('countries', function countriesService($http, $q) {
    var URLS = {
        FETCH: 'data/countries.json'
      },
      countries,
      currentCountry,
      countriesModel = this;

    function extract(result) {
      return result.data;
    }

    function cachecountries(result) {
      countries = extract(result);
      return countries;
    }

    countriesModel.getcountries = function () {
      return (countries) ? $q.when(countries) : $http.get(URLS.FETCH).then(cachecountries);
    };

    countriesModel.getCurrentCountry = function () {
      return currentCountry;
    };

    countriesModel.getCurrentCountryName = function () {
      return currentCountry ? currentCountry.name : '';
    };

    countriesModel.setCurrentCountry = function (country) {
      currentCountry = country;
      return currentCountry;
    };

    countriesModel.createCountry = function (country) {
      country.id = countries.length;
      countries.push(country);
    };

    countriesModel.deleteCountry = function (country) {
      _.remove(countries, function (c) {
        return c.id == country.id;
      });
    };

    countriesModel.getCountryByName = function (countryName) {
      var deferred = $q.defer();

      function findCountry() {
        return _.find(countries, function (c) {
          return c.name == countryName;
        })
      }

      if (countries) {
        deferred.resolve(findCountry());
      } else {
        countriesModel.getcountries().then(function () {
          deferred.resolve(findCountry());
        })
      }

      return deferred.promise;
    };

  })
;
