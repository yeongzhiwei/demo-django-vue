<template>
    <div class ="pagination">
        <a v-if="hasPrevious" href="#" v-on:click.stop="$emit('goto', previousPage)">&lt;&lt;&nbsp;</a>
        {{ currentPage }}
        <a v-if="hasNext" href="#" v-on:click.stop="$emit('goto', nextPage)">&gt;&gt;&nbsp;</a>
    </div>
</template>

<script>
export default {
    name: 'BasePagination',
    props: {
        hasPrevious: Boolean,
        hasNext: Boolean,
        currentPage: Number,
    },
    computed: {
        previousPage: function() {
            return this.currentPage - 1;
        },
        nextPage: function() {
            return this.currentPage + 1;
        },
    }
}
</script>
