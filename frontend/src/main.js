import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import * as VueGoogleMaps from 'vue2-google-maps'
import App from './App.vue';
import router from './router';

Vue.use(BootstrapVue);
Vue.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyBIAMgTl9-xvfUzmzG0FGbSIg4I2uKeWSU',
        libraries: 'places',
    }
});

Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App),
  }).$mount('#app');
