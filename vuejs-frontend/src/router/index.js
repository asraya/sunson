import Vue from 'vue'
import Router from 'vue-router'
import AllData from '@/components/all'
import Create from '@/components/create'
import Edit from '@/components/edit'
import Delete from '@/components/delete'
Vue.use(Router)
Vue.use(VueResource);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AllData',
      component: AllData
    },
    {
      path: '/create',
      name: 'Create',
      component: Create
    },
    {
      path: '/edit',
      name: 'EditEmployee',
      component: Edit
    },
    {
      path: '/delete',
      name: 'DeleteEmployee',
      component: Delete
    }
  ]
})
