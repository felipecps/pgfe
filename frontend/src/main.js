import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Calendar from 'v-calendar/lib/components/calendar.umd'
import DatePicker from 'v-calendar/lib/components/date-picker.umd'

import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.use(BootstrapVue);
Vue.component('calendar', Calendar)
Vue.component('date-picker', DatePicker)

Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App),
  }).$mount('#app');
