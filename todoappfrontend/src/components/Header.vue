<template>
    <div class="d-flex justify-content-between align-items-center mt-3 pb-2 border-bottom border-2 border-secodary ">
        <h3 class=" ms-5 text-dark">Task Reminder</h3>
        <Button :showAddForm="showAddForm" @click.prevent="$emit('toggleAddTask')"/>
    </div>
</template>

<script>
    import Button from './Button'
   

export default {
    name:'Header',
    data(){
        return{
            
        }
    },
    emits:['toggleAddTask'],
    components:{Button},
    props:{showAddForm:Boolean}
}
</script>