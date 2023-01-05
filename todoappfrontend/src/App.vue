<template >
  <div class="container bg-light d-flex justify-content-between flex-column mt-3 mb-3 border border-2 border-secondary rounded-3" style="min-height:30rem; max-width:30rem;">
    <Header @toggleAddTask="toggleAddTask" :showAddForm="showAddForm"/>
    <router-view :showAddForm="showAddForm"></router-view>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
  data(){
    return{
      showAddForm : false
    }
  },
  components:{Header,Footer},
  methods:{
    toggleAddTask(){
      this.showAddForm = !this.showAddForm
    }
  }
}
</script>
