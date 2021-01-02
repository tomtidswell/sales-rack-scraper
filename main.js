
import Vue from 'vue'
import App from './src/components/App.vue'

//remove these to remove buefy 
import Buefy from 'buefy'
Vue.use(Buefy)


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')