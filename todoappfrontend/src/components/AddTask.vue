<template>
    <form class="border-bottom border-bottom border-2 border-secodary p-3">
        <div class="form-group">
            <label for="task-name" class="text-dark fs-5">Task</label>
            <input v-model="name" id="task-name" type="text" class="form-control">
        </div>       
        <div class="form-group mt-3">
            <label for="task-day" class="text-dark fs-5">Day - Time</label>
            <input v-model="day" id="task-day" type="text" class="form-control ">
        </div>
        <div class="form-group mt-3">
            <label for="task-reminder" class="text-dark fs-5 d-flex">Reminder</label>
            <input v-model="reminder" id="task-reminder" type="checkbox">
        </div>
        <div class="form-group d-flex justify-content-end">
            <button @click.prevent="onSubmit()" class="btn btn-success d-flex justify-content-end">Save Task</button>
        </div>
    </form>
</template>

<script>
export default {
    name:'AddTask',
    data(){
        return {
            name:"",
            day:"",
            reminder:false
        }
    },
    methods:{
        onSubmit(){
            if(this.task === ''){
                alert('Please enter task before submitting..')
                return
            }
            const newTask = {
                // id:Math.floor(Math.random()*100000),
                name:this.name,
                day:this.day,
                reminder:this.reminder
            }
            this.$emit('addNewTask',newTask)
            this.name=''
            this.day=''
            this.reminder=false
        }
    }
    
}
</script>