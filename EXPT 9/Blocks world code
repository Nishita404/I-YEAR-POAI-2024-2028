class BlocksWorld:
    def __init__(self, num_blocks):
        # Initialize blocks world with each block on its own stack (on the table)
        self.state = [[block] for block in range(num_blocks)]
        self.num_blocks = num_blocks

    def display_state(self):
        print("Current state:")
        for i, stack in enumerate(self.state):
            print(f"Stack {i}: {stack}")

    def find_block(self, block):
        # Find the stack that contains the given block
        for stack in self.state:
            if block in stack:
                return stack
        return None

    def move(self, block, destination):
        # Move block onto the top of the destination block
        source_stack = self.find_block(block)
        destination_stack = self.find_block(destination)

        if source_stack is None or destination_stack is None:
            print(f"Invalid block {block} or destination {destination}.")
            return

        if source_stack[-1] != block:
            print(f"Block {block} is not on top of its stack, cannot move.")
            return

        # Remove the block from its current stack
        source_stack.remove(block)

        # Place it on top of the destination stack
        destination_stack.append(block)

        print(f"\nMoved block {block} onto block {destination}.")
        self.display_state()

    def goal_state(self, goal):
        # Display goal state for visual reference (no solving logic)
        print("\nGoal state (for reference only):")
        for i, stack in enumerate(goal):
            print(f"Stack {i}: {stack}")

def main():
    # Initialize Blocks World with 3 blocks
    blocks_world = BlocksWorld(3)
    print("Initial state:")
    blocks_world.display_state()

    # Define the goal configuration
    goal = [[1, 0], [2]]  # e.g., block 0 on block 1, block 2 on table
    blocks_world.goal_state(goal)

    print("\nPerforming Moves:")
    # Example moves
    blocks_world.move(0, 2)  # Move block 0 onto block 2
    blocks_world.move(0, 1)  # Move block 0 onto block 1
    blocks_world.move(2, 0)  # Try invalid move (block 2 not on top)

if __name__ == "__main__":
    main()
