angular.module('childsoldier', [
  'ngAnimate',
  'ui.router',
  'countries',
  'reports'
])
  .config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('childsoldier', {
        url: '',
        abstract: true
      })
    ;
    $urlRouterProvider.otherwise('/');
  })

;