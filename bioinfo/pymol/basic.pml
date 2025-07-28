# Basic usage

reinitalize
fetch xxxx

select A, chain A
select B, chain A + chain B

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
ray 1000, 1000
png xxx.png, dpi=300

set_view()
get_view()


