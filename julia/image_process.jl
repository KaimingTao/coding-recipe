### A Pluto.jl notebook ###
# v0.20.9

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    #! format: off
    return quote
        local iv = try Base.loaded_modules[Base.PkgId(Base.UUID("6e696c72-6542-2067-7265-42206c756150"), "AbstractPlutoDingetjes")].Bonds.initial_value catch; b -> missing; end
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : iv(el)
        el
    end
    #! format: on
end

# ╔═╡ af2035ba-f1fb-43f5-b8b7-abab6753f5d0
import Pkg

# ╔═╡ 57a2f2c9-7a0b-47ff-9987-b967de49f352
Pkg.add("Images")

# ╔═╡ 8b03860d-482d-42ff-bd0a-abe991a37055
Pkg.add("DSP")

# ╔═╡ d3ec2d68-02fa-4d04-b4ea-6223e049ea9c
Pkg.add("LinearAlgebra")

# ╔═╡ 9fa27906-7414-11f0-26ce-79d83c1456bd
using Images

# ╔═╡ 744c376a-7d90-4b8f-8d05-17353871ae33
using ImageEdgeDetection

# ╔═╡ 8a199165-20f2-49cd-9838-d09cb13fa0c1
using ImageIO

# ╔═╡ 6a997b49-1a42-4d22-846b-0335b907373f
using LinearAlgebra

# ╔═╡ ed6da970-85ab-4180-9778-b5def1e647ff
# url = "https://images.unsplash.com/photo-1753803203615-e06cb3266079?q=80&w=1168&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# ╔═╡ eaffcc95-6a99-472a-89d9-c041be1b3f72
# download(url, "bird.jpg")

# ╔═╡ ddea9955-f640-469c-9693-51c84e0661fb
bird = load("bird.jpg")

# ╔═╡ 197b0455-6d1b-4bac-bdce-948868c169d9
bird

# ╔═╡ aafa92f2-65f7-4425-bf33-1c6986989e57
typeof(bird)

# ╔═╡ b708f6cf-c341-4403-bde9-6bea51e78898
RGBX(0.9,0.6,0.1)

# ╔═╡ 08eee69f-cd04-454a-89b4-9bb0ff4db38f
size(bird)

# ╔═╡ 42efbfd1-bb44-48b4-a371-cbffd59fa440
bird[200:500, 200:500]

# ╔═╡ c8350d5e-895d-4186-8194-3fca96cef413
begin
	(h, w) = size(bird)
	part = bird[100: (h ÷ 2) + 100, 100: (w ÷ 2) + 100]
end

# ╔═╡ 8b9e8c65-324d-44e5-b64c-b2669eb4a4d6
[part part]

# ╔═╡ 4168e1fa-b1d4-4769-8eef-f6fa1e170b22
[
	part                  reverse(part, dims=2)
	reverse(part, dims=1) reverse(reverse(part, dims=1), dims=2)
]

# ╔═╡ ea83a278-4367-4131-8509-e1834cf1de9e
 bird2 = copy(bird)

# ╔═╡ 86a5017b-67f0-4ba8-8441-fa5c413e18fa
for i in 1:100
	for j in 1:300
		bird2[i, j] = RGB(1,0,0)
	end
end

# ╔═╡ 96a371ae-0a24-48f7-87c1-f3168345cf05
bird2

# ╔═╡ bf1ecad2-567d-476b-a135-6851d5732725
bird2[200:300, 200:300] .= RGB(0,1,0)

# ╔═╡ 19da3e38-3af8-4de7-bcbc-ba4e7b2eaf86
bird2

# ╔═╡ 51b60811-a318-46d5-9098-e2bd3e9f3480
function redify(c)
	return RGB(c.r, 0, 0)
end

# ╔═╡ bcd3aec8-c91f-40ff-946d-07c1c5e4aca7
begin
	color = RGB(0.4, 0.6, 0.6)
	[color, redify(color)]
end

# ╔═╡ 5fcdb2f8-8734-4e98-8052-04f9f4d014c6
redify.(bird)

# ╔═╡ e534fe54-aaed-4d45-b440-6eabfd494fed
# using PlutoUI

# ╔═╡ 43a39475-b517-41be-a776-b85862050fd5
# @bind raw_camera_data camera_input()
# Not working

# ╔═╡ 553567a9-35ab-4b10-82f1-9dedc8f65e95


# ╔═╡ 7e052b98-15a0-4d8e-b77d-a23cfe74d663
detect_edges(bird)

# ╔═╡ 2dae0976-106e-4591-b909-34447302507e


# ╔═╡ 761352f7-54a2-4c5c-96d3-4ed899afc37a


# ╔═╡ Cell order:
# ╠═9fa27906-7414-11f0-26ce-79d83c1456bd
# ╠═ed6da970-85ab-4180-9778-b5def1e647ff
# ╠═eaffcc95-6a99-472a-89d9-c041be1b3f72
# ╠═ddea9955-f640-469c-9693-51c84e0661fb
# ╠═197b0455-6d1b-4bac-bdce-948868c169d9
# ╠═aafa92f2-65f7-4425-bf33-1c6986989e57
# ╠═b708f6cf-c341-4403-bde9-6bea51e78898
# ╠═08eee69f-cd04-454a-89b4-9bb0ff4db38f
# ╠═42efbfd1-bb44-48b4-a371-cbffd59fa440
# ╠═c8350d5e-895d-4186-8194-3fca96cef413
# ╠═8b9e8c65-324d-44e5-b64c-b2669eb4a4d6
# ╠═4168e1fa-b1d4-4769-8eef-f6fa1e170b22
# ╠═ea83a278-4367-4131-8509-e1834cf1de9e
# ╠═86a5017b-67f0-4ba8-8441-fa5c413e18fa
# ╠═96a371ae-0a24-48f7-87c1-f3168345cf05
# ╠═bf1ecad2-567d-476b-a135-6851d5732725
# ╠═19da3e38-3af8-4de7-bcbc-ba4e7b2eaf86
# ╠═51b60811-a318-46d5-9098-e2bd3e9f3480
# ╠═bcd3aec8-c91f-40ff-946d-07c1c5e4aca7
# ╠═5fcdb2f8-8734-4e98-8052-04f9f4d014c6
# ╠═e534fe54-aaed-4d45-b440-6eabfd494fed
# ╠═43a39475-b517-41be-a776-b85862050fd5
# ╠═af2035ba-f1fb-43f5-b8b7-abab6753f5d0
# ╠═57a2f2c9-7a0b-47ff-9987-b967de49f352
# ╠═744c376a-7d90-4b8f-8d05-17353871ae33
# ╠═8a199165-20f2-49cd-9838-d09cb13fa0c1
# ╠═553567a9-35ab-4b10-82f1-9dedc8f65e95
# ╠═7e052b98-15a0-4d8e-b77d-a23cfe74d663
# ╠═8b03860d-482d-42ff-bd0a-abe991a37055
# ╠═2dae0976-106e-4591-b909-34447302507e
# ╠═d3ec2d68-02fa-4d04-b4ea-6223e049ea9c
# ╠═6a997b49-1a42-4d22-846b-0335b907373f
# ╠═761352f7-54a2-4c5c-96d3-4ed899afc37a
