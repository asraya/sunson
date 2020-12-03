import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource';

Vue.config.productionTip = false
Vue.http.options.emulateJSON = true;

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
