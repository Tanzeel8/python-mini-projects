import random
import time

def simulate_team(num_runners=4, min_time=0.8, max_time=2.0):
    """Simulate one team's relay: return total time and list of individual times."""
    times = []
    total = 0.0
    for i in range(1, num_runners+1):
        t = random.uniform(min_time, max_time)
        times.append(t)
        total += t
    return total, times

def main():
    random.seed()  # system time seed
    teams = {
        "Red": 4,
        "Blue": 4,
        "Green": 4
    }

    results = {}
    print("Starting simple relay race simulation...\n")
    for team_name, runners in teams.items():
        total, times = simulate_team(runners)
        results[team_name] = (total, times)
        print(f"Team {team_name} times: " + ", ".join(f"{t:.2f}s" for t in times) + f"  => total {total:.2f}s")
        time.sleep(0.5)

    # Determine winner
    winner = min(results.items(), key=lambda kv: kv[1][0])
    print(f"\n🏁 Winner: {winner[0]} with {winner[1][0]:.2f}s")

if __name__ == "__main__":
    main()
