<template>
  <AddTask v-show="showAddForm" @addNewTask="addNewTask"/>
  <Tasks @deleteTask="deleteTask" @reminderToggle="reminderToggle" :tasks='tasks'/>
</template>

<script>
// @ is an alias to /src
import AddTask from '../components/AddTask'
import Tasks from '../components/Tasks'
import axios from 'axios'

export default {
  
  name: 'HomeView',
  data(){
    return{
      tasks : [],      
    }
  },
  async created(){
    await this.getTasks()
    this.tasks.sort((a, b) => b.id-a.id)
  },
  components: {AddTask,Tasks},
  props:{showAddForm:Boolean},
  methods:{
    async reminderToggle(id){        
      this.tasks.forEach(task=>{
        if (task.id === id){                  
          task.reminder = !task.reminder
          axios.put(`api/v1/todo/${id}`,task)                    
        }
      })
    },
    async deleteTask(id){
      this.tasks.forEach(task=>{
        if (task.id === id){
          axios.delete(`api/v1/todo/${id}`)
          this.tasks.splice(this.tasks.indexOf(task),1)
        }
      })
    },
    async addNewTask(task){      
      axios.post('api/v1/todo/',task)
      this.tasks.unshift(task)
    },
    async getTasks(){
        await axios
          .get('api/v1/todo')
          .then(response=>{
            this.tasks = response.data                               
          }) 
    }    
  }
}
</script>
