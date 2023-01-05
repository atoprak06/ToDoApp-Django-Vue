<template>
    <div v-for="task in tasks" :key="task.id">
        <Task @deleteTask="$emit('deleteTask',task.id)" @reminderToggle="$emit('reminderToggle',task.id)" :task = 'task'/>
    </div>        
</template>

<script>
import Task from './Task'
export default {
    name:'Tasks',
    props:{tasks:Array},
    components:{Task},
    emits:['reminderToggle','deleteTask']

}
</script>