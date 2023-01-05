<template>
    <button :class="[showAddForm ? 'btn-danger':'btn-primary','btn']">{{showAddForm?'Close':'Add'}}</button>
</template>

<script>
export default {
    name:'Button',
    props:{showAddForm:Boolean}
}
</script>