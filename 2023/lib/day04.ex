defmodule Aoc2023.Day04 do
  alias Aoc2023

  def part1(input) do
    input
    |> parse_input()
    |> Enum.reject(fn x -> String.contains?(x, "Card") end)
    |> Enum.flat_map(fn s -> String.split(s, " | ") end)
    |> Enum.map(fn s -> String.split(s) |> MapSet.new() end)
    |> Enum.chunk_every(2)
    |> Enum.reduce([], fn [winning, owned], acc ->
      [MapSet.intersection(winning, owned) | acc]
    end)
    |> Enum.reject(fn ms -> MapSet.size(ms) == 0 end)
    |> Enum.map(fn ms -> 2 ** (MapSet.size(ms) - 1) end)
    |> Enum.sum()
  end

  def part2(input) do
    input
    |> parse_input()
    |> Enum.reject(fn x -> String.contains?(x, "Card") end)
    |> Enum.map(&map_card_size/1)
    |> Enum.with_index()
    |> Map.new(fn {w, i} -> {i, w} end)
  end

  defp run_game(input, all_cards, current, max) do
  end

  defp map_card_size(card) do
    card
    |> String.split(" | ")
    |> Enum.map(fn s -> String.split(s) |> MapSet.new() end)
    |> Enum.chunk_every(2)
    |> Enum.reduce([], fn [winning, owned], acc ->
      [MapSet.intersection(winning, owned) | acc]
    end)
    |> Enum.map(fn ms -> MapSet.size(ms) end)
    |> Enum.sum()
  end

  defp parse_input(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.flat_map(&String.split(&1, ": ", trim: true))
  end

  def example1() do
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
  end

  def part1_ex_verify, do: example1() |> part1()
  def part2_ex_verify, do: example1() |> part2()

  def part1_verify, do: Aoc2023.input("04") |> part1()
  def part2_verify, do: Aoc2023.input("04") |> part2()
end
