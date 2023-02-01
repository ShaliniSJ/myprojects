<script>
	let newitem = "";
	let todolist = [];
	function addlist(){
		todolist = [...todolist,{item : newitem,status : false}];
		newitem = "";
	}
	function remove(index){
		todolist.splice(index,1);
		todolist = todolist;
	}
</script>
<h1>
	To do list
</h1>
<input type = "text" bind:value = {newitem} placeholder = "add an task">
<button on:click = {addlist}> add </button> 
<br>
{#each todolist as items,index}
	<input bind:checked = {items.status} type = "checkbox" >
	<span class:checked = {items.status} >{items.item}</span>
	<span class = "red" on:click = {()=> remove(index)} >☒</span>
<br>
{/each}

<style>
	.red{
		color : red
	}
	span {
		color : blue;
	}
	.checked{
		color : green;
		text-decoration : line-through;
	}
</style>
