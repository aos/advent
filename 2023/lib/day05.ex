defmodule Aoc2023.Day05 do
  alias Aoc2023

  def part1(input) do
    dictionary = parse_input(input)
    find_min_location(dictionary, dictionary.seeds)
  end

  def part2(input) do
    dictionary = parse_input(input)
    seeds =
      dictionary.seeds
      |> Enum.chunk_every(2)
      |> Enum.map(fn [f, s] -> f..(f + s) end)
      |> IO.inspect(label: "SEED RANGE")
      |> Enum.flat_map(&Range.to_list/1)
    find_min_location(dictionary, seeds)
  end

  def find_min_location(dictionary, seeds) do
    seeds
    |> Enum.map(fn seed -> 
      categories()
      |> Enum.reduce(seed, fn cat, acc ->
        item = 
          dictionary[cat]
          |> Enum.find(fn {start, %{range: range}} ->
            acc in start..(start + range - 1)
          end)

        case item do
          {start, %{dest: dest}} -> acc - start + dest
          _ -> acc
        end
      end)
    end)
    |> Enum.min()
  end

  # seeds: [ ]
  # soil: %{ source => %{ dest: integer, range: integer } }
  def parse_input(input) do
    input
    |> String.split("\n\n", trim: true)
    |> Enum.map(fn s ->
      case String.split(s, ":", trim: true) do
        ["seeds", output] ->
          %{seeds: map_seeds(output)}

        [name, output] ->
          [_, _, key] = String.split(name, "-")
          [name, _] = String.split(key, " ", trim: true)
          %{String.to_atom(name) => map_category(output)}
      end
    end)
    |> Enum.reduce(%{}, fn m, acc -> Map.merge(acc, m) end)
  end

  defp map_seeds(input) do
    input
    |> String.split(" ", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  # %{soil:
  #     %{83: %{dest: 50, range: 2}},
  #     %{50: %{dest: 52, range: 48}}}
  defp map_category(input) do
    input
    |> String.split("\n", trim: true)
    |> Enum.map(fn map ->
      [dest, source, range] =
        map
        |> String.split(" ", trim: true)
        |> Enum.map(&String.to_integer/1)

      %{source => %{dest: dest, range: range}}
    end)
    |> Enum.reduce(%{}, fn m, acc -> Map.merge(acc, m) end)
  end

  def categories() do
    ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    |> Enum.map(&String.to_atom/1)
  end

  def example1() do
    "seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"
  end

  def part1_ex_verify, do: example1() |> part1()
  def part2_ex_verify, do: example1() |> part2()

  def part1_verify, do: Aoc2023.input("05") |> part1()
  def part2_verify, do: Aoc2023.input("05") |> part2()
end
