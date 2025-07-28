# Basic usage

reinitalize
fetch xxxx
as cartoon
util.cbc


## Assemly structure

set assembly, 1
# sometimes the assembly is not working, try this:
# set all_states, on
fetch 5T3Z
split_states 5T3Z


## Selection

sele color cyan
set_name sele, RBD

select A, chain A
select B, chain A + chain B
select C, chain A and resi 1+2+300

iterate (xxx), print(f"Chain: {chain}, Resi: {resi}, Resn: {resn}")
sele xxx, yyy within 2.5 of chain A

create C, chain A and resi 1-100

show surface, xxx

show cartoon, xxx
cartoon tube, xxx
color gray80, xxx
set transparency, 0.5, xxx
color 0x000000, xxx


set ray_opaque_background, on
bg white
ray 1000, 1000
png xxx.png, dpi=300

set_view()
get_view()


