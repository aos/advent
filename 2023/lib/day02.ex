defmodule Aoc2023.Day02 do
  alias Aoc2023

  def part1(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_game/1)
    |> Enum.with_index()
    |> Enum.filter(fn {x, _idx} ->
      not Enum.any?([
        12 - x[:red] < 0,
        14 - x[:blue] < 0,
        13 - x[:green] < 0
      ])
    end)
    |> Enum.reduce(0, fn {_x, idx}, acc -> acc + 1 + idx end)
  end

  def example_1 do
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
  end

  # turns the game into a map: %{red: 20, blue: 4, green: 9}
  def parse_game(string) do
    string
    |> String.split(": ")
    |> Enum.reject(fn x -> String.contains?(x, "Game") end)
    |> Enum.flat_map(&String.split(&1, ";"))
    |> Enum.flat_map(&String.split(&1, ","))
    |> Enum.map(&String.trim/1)
    |> Enum.reduce(%{}, fn x, acc ->
      [num, color] = String.split(x, " ")

      {_, updated} =
        Map.get_and_update(acc, String.to_atom(color), fn current ->
          if is_nil(current) do
            {current, String.to_integer(num)}
          else
            {current, max(current, String.to_integer(num))}
          end
        end)

      updated
    end)
  end
end
