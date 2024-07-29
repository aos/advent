defmodule Aoc2023Test do
  use ExUnit.Case
  doctest Aoc2023

  describe "Day 02" do
    import Aoc2023.Day02

    test "part 1 - example" do
      example_1()
      |> part1()
      |> then(fn x -> assert x == 8 end)
    end
  end
end
