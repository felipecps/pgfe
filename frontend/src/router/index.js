import Vue from 'vue'
import VueRouter from 'vue-router'
import Ping from '../views/Ping.vue';
import PaginaInicial from '../views/PaginaInicial.vue';
import EmailAlert from '../views/EmailAlert.vue';
import CalculaCorretagem from '../views/CalculaCorretagem.vue';
import PythonExercicios from '../views/Python.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'PaginaInicial',
        component: PaginaInicial,
  },
  {
    path: '/emailalert',
    name: 'EmailAlert',
    component: EmailAlert,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/calculacorretagem',
    name: 'CalculaCorretagem',
    component: CalculaCorretagem,
   },
   {
    path: '/python',
    name: 'PythonExercicios',
    component: PythonExercicios,
   }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
