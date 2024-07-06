defmodule Aoc2023 do
  @input_path "./in/day"

  def input(day) do
    File.read!(@input_path <> day <> ".txt")
  end
end
