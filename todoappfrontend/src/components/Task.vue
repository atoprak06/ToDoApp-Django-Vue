<template>
    <div @dblclick="$emit('reminderToggle',task.id)" class="card mb-3 mt-3">      
        <div :class="[task.reminder ? 'border-start border-success border-4':'','card-body']">
            <div class="d-flex justify-content-between">
                <p class="fs-3 border-bottom border-secondary border-2 m-0">{{task.name}}</p>
                <i @click="$emit('deleteTask',task.id)" class="fa-solid fa-xmark text-danger fs-5"></i>
            </div>
            <p class="fs-5 m-0">{{task.day}}</p>            
        </div>
    </div>
</template>

<script>
export default {
    name:'Task',
    props:{task:Object},
    emits:['reminderToggle','deleteTask']
}
</script>